part of 'login_bloc.dart';

//ignore_for_file: non_constant_identifier_names

class LoginState extends Equatable {
  final int step;
  final bool loading;
  final OtpResponse otpResponse;
  final dynamic errors;

  const LoginState({
    this.loading = false,
    this.otpResponse,
    this.errors,
    this.step,
  });

  factory LoginState.initial() {
    return LoginState(step: 0);
  }

  LoginState copyWith({
    int step,
    bool loading,
    OtpResponse otpResponse,
    dynamic errors,
  }) {
    return LoginState(
        step: step ?? this.step,
        loading: loading ?? this.loading,
        otpResponse: otpResponse ?? this.otpResponse,
        errors: errors ?? this.errors);
  }

  @override
  List<Object> get props => [step, loading, errors];
}
