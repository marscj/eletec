part of 'email_login_bloc.dart';

abstract class EmailLoginState extends Equatable {
  const EmailLoginState();
}

class EmailLoginInitial extends EmailLoginState {
  @override
  List<Object> get props => [];
}
