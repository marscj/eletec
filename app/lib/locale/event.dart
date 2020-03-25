part of 'locale.dart';

abstract class LocaleEvent {
  final Locale locale;

  const LocaleEvent(this.locale);
}

class LocaleInit extends LocaleEvent {
  LocaleInit(Locale locale) : super(locale);
}

class LocaleUpdate extends LocaleEvent {
  LocaleUpdate(Locale locale) : super(locale);
}
