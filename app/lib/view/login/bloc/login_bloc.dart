import 'dart:async';

import 'package:bloc/bloc.dart';
import 'package:equatable/equatable.dart';
import 'package:rxdart/rxdart.dart';

part 'login_event.dart';
part 'login_state.dart';

//ignore_for_file: close_sinks

class LoginBloc extends Bloc<LoginEvent, LoginState> {
  final Sink<String> phoneSink;
  final Sink<String> otpSink;

  factory LoginBloc() {
    final _phoneSink = BehaviorSubject<String>()..listen((onData) {});
    final _otpSink = BehaviorSubject<String>()..listen((onData) {});

    return LoginBloc._(_phoneSink, _otpSink);
  }

  LoginBloc._(this.phoneSink, this.otpSink);

  @override
  LoginState get initialState => LoginState.initial();

  @override
  Stream<LoginState> mapEventToState(
    LoginEvent event,
  ) async* {
    if (event is LoginGetOTP) {
      yield state.copyWith(step: 1);
    }

    if (event is LoginResendOTP) {
      yield state.copyWith(
        step: 0,
        otp: '',
      );
    }
  }

  @override
  Future<void> close() {
    phoneSink.close();
    otpSink.close();
    return super.close();
  }
}
