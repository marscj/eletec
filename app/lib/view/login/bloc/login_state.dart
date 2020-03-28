part of 'login_bloc.dart';

abstract class LoginState extends Equatable {
  const LoginState();

  @override
  List<Object> get props => [];
}

class LoginInitState extends LoginState {}

class LoginOtpState extends LoginState {}

class LoginSuccess extends LoginState {}
