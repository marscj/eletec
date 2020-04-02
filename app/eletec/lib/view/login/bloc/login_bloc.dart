import 'dart:async';

import 'package:bloc/bloc.dart';
import 'package:eletec/plugs/flutter_form_builder/flutter_form_builder.dart';
import 'package:eletec/rest/client.dart';
import 'package:equatable/equatable.dart';
import 'package:flutter/material.dart';

part 'login_event.dart';
part 'login_state.dart';

class LoginBloc extends Bloc<LoginEvent, LoginState> {
  final GlobalKey<FormBuilderState> formKey = GlobalKey<FormBuilderState>();

  @override
  LoginState get initialState => LoginState.initial();

  @override
  Stream<LoginState> mapEventToState(
    LoginEvent event,
  ) async* {
    if (event is GetOTP) {
      if (formKey.currentState.saveAndValidate()) {
        yield state.copyWith(loading: true);

        RestService.instance.phoneGenerate(formKey.currentState.value).then((res) {
          add(ResponseOTP(res));
        }).catchError((error) {
          formKey.currentState.setErrors(error?.response?.data);
        });
      }
    }

    if (event is ResponseOTP) {
      yield state.copyWith(
        step: 1, 
        loading: false,
        otp: event.result
      );
    }

    if (event is ResendOTP) {
      yield state.copyWith(
        step: 0
      );
    }

    if (event is FormSubmitted) {
      if (formKey.currentState.saveAndValidate()) {
        yield state.copyWith(loading: true);

        RestService.instance.phoneValidate(formKey.currentState.value).then((res) {
          add(ResponseOTP(res));
        }).catchError((error) {
          formKey.currentState.setErrors(error?.response?.data);
        });
      }
    }
  }

  @override
  Future<void> close() {
    return super.close();
  }
}
