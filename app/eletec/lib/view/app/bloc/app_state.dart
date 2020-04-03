part of 'app_bloc.dart';

class AppState extends Equatable {

  final bool hasToken;

  final Locale locale;

  final String tag;

  @override
  List<Object> get props => [hasToken, locale.languageCode, tag];

  AppState({
    this.hasToken,
    this.locale,
    this.tag
  });

  factory AppState.initial() => AppState();

  AppState copyWith({
    bool hasToken,
    Locale locale,
    String tag,
  }) => AppState(
    hasToken: hasToken ?? this.hasToken,
    locale: locale ?? this.locale,
    tag: tag ?? this.tag
  );
}
