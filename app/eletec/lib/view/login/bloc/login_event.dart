part of 'login_bloc.dart';

// ignore_for_file: non_constant_identifier_names

abstract class LoginEvent extends Equatable {
  const LoginEvent();

  @override
  List<Object> get props => [];
}

class GetOTP extends LoginEvent {}

class ResponseOTP extends LoginEvent {
  final dynamic result;

  ResponseOTP(this.result);
}

class Timer extends LoginEvent {
  final int timer;

  Timer(this.timer);
}

class ResendOTP extends LoginEvent {}

class FormSubmitted extends LoginEvent {}
