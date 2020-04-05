part of 'app_bloc.dart';

class AppState extends Equatable {

  final bool signedIn;

  final Locale locale;

  @override
  List<Object> get props => [signedIn, locale.languageCode];

  AppState({
    this.signedIn,
    this.locale,
  });

  factory AppState.initial() => AppState(
    signedIn: false,
    locale: Locale('en', ''),
  );

  AppState copyWith({
    bool signedIn,
    Locale locale,
  }) => AppState(
    signedIn: signedIn ?? this.signedIn,
    locale: locale ?? this.locale,
  );
}
