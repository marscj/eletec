part of 'login_bloc.dart';

// ignore_for_file: non_constant_identifier_names

abstract class LoginEvent extends Equatable {
  const LoginEvent();

  @override
  List<Object> get props => [];
}

class GetOtp extends LoginEvent {}

class BackStep extends LoginEvent {}

class FormSubmitted extends LoginEvent {}

class PhoneNumberChange extends LoginEvent {
  final String phone_number;

  PhoneNumberChange(this.phone_number);

  @override
  List<Object> get props => [phone_number];
}

class StateChange extends LoginEvent {
  final String phone_number;
  final String otp;

  StateChange({this.phone_number, this.otp});

  @override
  List<Object> get props => [otp];
}
