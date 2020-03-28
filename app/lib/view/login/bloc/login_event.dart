part of 'login_bloc.dart';

// ignore_for_file: non_constant_identifier_names

abstract class LoginEvent extends Equatable {
  const LoginEvent();

  @override
  List<Object> get props => [];
}

class LoginGetOTP extends LoginEvent {
  final String phone_number;

  LoginGetOTP(this.phone_number);

  @override
  List<Object> get props => [phone_number];
}

class LoginResendOTP extends LoginEvent {}

class LoginValidate extends LoginEvent {
  final String phone_number;
  final String otp;

  LoginValidate(this.phone_number, this.otp);

  @override
  List<Object> get props => [phone_number, otp];
}
