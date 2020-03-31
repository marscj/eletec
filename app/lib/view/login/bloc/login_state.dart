part of 'login_bloc.dart';

//ignore_for_file: non_constant_identifier_names

class LoginState extends Equatable {
  final int step;
  final bool loading;
  final Map<String, dynamic> error;

  const LoginState({
    this.loading = false,
    this.error,
    this.step,
  });

  factory LoginState.initial() {
    return LoginState(step: 0);
  }

  LoginState copyWith({
    int step,
    bool loading,
    Map<String, dynamic> error,
  }) {
    return LoginState(
        step: step ?? this.step,
        loading: loading ?? this.loading,
        error: error ?? this.error);
  }

  @override
  List<Object> get props => [step, loading, error];
}
