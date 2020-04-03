part of 'app_bloc.dart';

class AppState extends Equatable {

  final bool hasToken;

  final Locale locale;

  @override
  List<Object> get props => [hasToken, locale.languageCode];

  AppState({
    this.hasToken,
    this.locale,
  });

  factory AppState.initial() => AppState(
    hasToken: false,
    locale: Locale('en', ''),
  );

  AppState copyWith({
    bool hasToken,
    Locale locale,
  }) => AppState(
    hasToken: hasToken ?? this.hasToken,
    locale: locale ?? this.locale,
  );
}
