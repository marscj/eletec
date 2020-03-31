part of 'login_bloc.dart';

// ignore_for_file: non_constant_identifier_names

abstract class LoginEvent extends Equatable {
  const LoginEvent();

  @override
  List<Object> get props => [];
}

class GetOTP extends LoginEvent {}

class ResendOTP extends LoginEvent {}

class FormSubmitted extends LoginEvent {}
