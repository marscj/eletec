part of 'login_bloc.dart';

//ignore_for_file: non_constant_identifier_names

class LoginState extends Equatable {
  final int step;
  final bool loading;
  final Otp otp;
  final Token token;
  final dynamic errors;
  final int timer;

  const LoginState({
    this.loading = false,
    this.otp,
    this.token,
    this.errors,
    this.step,
    this.timer = 0,
  });

  factory LoginState.initial() {
    return LoginState(step: 0);
  }

  LoginState copyWith({
    int step,
    bool loading,
    Otp otp,
    Token token,
    dynamic errors,
    int timer
  }) {
    return LoginState(
      step: step ?? this.step,
      loading: loading ?? this.loading,
      otp: otp ?? this.otp,
      token: token ?? this.token,
      errors: errors ?? this.errors,
      timer: timer ?? this.timer
    );
  }

  @override
  List<Object> get props => [step, loading, errors, timer];
}
