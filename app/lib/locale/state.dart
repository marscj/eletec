part of 'locale.dart';

class LocaleState {
  final Locale locale;

  const LocaleState(this.locale);

  factory LocaleState.inital() => LocaleState(Locale('en', ''));
}
