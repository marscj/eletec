part of 'login_bloc.dart';

//ignore_for_file: non_constant_identifier_names

class LoginState extends Equatable {
  final String phone_number;
  final String otp;
  final int step;
  final bool successful;

  const LoginState({
    this.phone_number,
    this.otp,
    this.step,
    this.successful,
  });

  factory LoginState.initial() {
    return LoginState(phone_number: '', otp: '', step: 1, successful: false);
  }

  LoginState copyWith({
    String phone_number,
    String otp,
    int step,
    bool successful,
  }) {
    return LoginState(
        phone_number: phone_number ?? this.phone_number,
        otp: otp ?? this.otp,
        step: step ?? this.step,
        successful: successful ?? this.successful);
  }

  @override
  List<Object> get props => [phone_number, otp, step, successful];
}
