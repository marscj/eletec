part of 'phone_login_bloc.dart';

abstract class PhoneLoginState extends Equatable {
  const PhoneLoginState();
}

class PhoneLoginInitial extends PhoneLoginState {
  @override
  List<Object> get props => [];
}
