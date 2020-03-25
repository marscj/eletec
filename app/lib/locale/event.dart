part of 'locale.dart';

abstract class LocaleEvent {}

class LocaleInit extends LocaleEvent {}

class LocaleUpdate extends LocaleEvent {
  final Locale locale;

  LocaleUpdate(this.locale);
}
