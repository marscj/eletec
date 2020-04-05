part of 'user_login_bloc.dart';

abstract class UserLoginState extends Equatable {
  const UserLoginState();
}

class UserLoginInitial extends UserLoginState {
  @override
  List<Object> get props => [];
}
