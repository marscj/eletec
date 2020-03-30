import 'dart:async';

import 'package:bloc/bloc.dart';
import 'package:equatable/equatable.dart';
import 'package:flutter/material.dart';

part 'login_event.dart';
part 'login_state.dart';

class LoginBloc extends Bloc<LoginEvent, LoginState> {
  TextEditingController phoneController;
  TextEditingController otpController;

  LoginBloc() {
    phoneController = TextEditingController()
      ..addListener(() {
        add(OnTextChange());
      });

    otpController = TextEditingController()
      ..addListener(() {
        add(OnTextChange());
      });
  }

  LoginBloc._(this.phoneController, this.otpController);

  @override
  LoginState get initialState => LoginState.initial();

  @override
  Stream<LoginState> mapEventToState(
    LoginEvent event,
  ) async* {
    if (event is GetOTP) {
      otpController.clear();
      yield state.copyWith(
        step: 1,
        otp: '',
      );
    }

    if (event is ResendOTP) {
      otpController.clear();
      yield state.copyWith(
        step: 0,
        otp: '',
      );
    }

    if (event is OnTextChange) {
      yield state.copyWith(
        phone_number: phoneController.text,
        otp: otpController.text,
      );
    }
  }

  @override
  Future<void> close() {
    phoneController.dispose();
    otpController.dispose();
    return super.close();
  }
}
