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
      yield state;

      if (formKey.currentState.saveAndValidate()) {
        yield state.copyWith(loading: true);

        RestService.instance.phoneGenerate({
          'phone_number': formKey.currentState.value['phone_number']
        }).then((res) {
          add(ResponseOTP(res, true));
        }).catchError((error) {
          add(ResponseOTP(error?.response?.data, false));
          formKey.currentState.setValidators(error?.response?.data);
        });
      }
    }

    if (event is ResponseOTP) {
      if (event.success ){
        yield state.copyWith(
          step: 1, 
          loading: false,
          otpResponse: event.result
        );
      } else {
        formKey.currentState.validate();
        yield state.copyWith(
          loading: false,
          errors: event.result
        );
      }
    }

    if (event is ResendOTP) {
      formKey.currentState.reset();
      yield state.copyWith(
        step: 0,
      );
    }

    if (event is FormSubmitted) {
      if (formKey.currentState.saveAndValidate()) {
        print(formKey.currentState.value);
      } else {
        print(formKey.currentState.value);
        print("validation failed");
      }
    }
  }

  @override
  Future<void> close() {
    return super.close();
  }
}
