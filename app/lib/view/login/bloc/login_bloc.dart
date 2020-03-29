import 'dart:async';

import 'package:bloc/bloc.dart';
import 'package:equatable/equatable.dart';
import 'package:flutter/material.dart';
import 'package:rxdart/rxdart.dart';

part 'login_event.dart';
part 'login_state.dart';

//ignore_for_file: close_sinks

class LoginBloc extends Bloc<LoginEvent, LoginState> {
  TextEditingController phoneController;
  TextEditingController otpController;

  LoginBloc() {
    phoneController = TextEditingController()
      ..addListener(() {
        add(StateChange(phone_number: phoneController.text));
      });

    otpController = TextEditingController()
      ..addListener(() {
        add(StateChange(otp: otpController.text));
      });

    // return LoginBloc._(_phoneController, _otpController);
  }

  LoginBloc._(this.phoneController, this.otpController);

  @override
  LoginState get initialState => LoginState.initial();

  @override
  Stream<LoginState> mapEventToState(
    LoginEvent event,
  ) async* {
    if (event is GetOtp) {
      yield state.copyWith(
        step: 1,
        // otp: '',
      );
    }

    if (event is BackStep) {
      yield state.copyWith(
        step: 0,
        // otp: '',
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
