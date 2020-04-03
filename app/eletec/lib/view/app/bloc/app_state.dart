part of 'app_bloc.dart';

class AppState extends Equatable {
  final String token;

  final Locale locale;

  @override
  List<Object> get props => [token];

  AppState({
    this.token,
    this.locale,
  });

  factory AppState.initial() => AppState();
}
