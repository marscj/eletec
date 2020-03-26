part of 'locale_bloc.dart';

abstract class LocaleEvent extends Equatable {
  final Locale locale;

  const LocaleEvent(this.locale);
}

class LocaleInit extends LocaleEvent {
  LocaleInit(Locale locale) : super(locale);

  @override
  List<Object> get props => null;
}

class LocaleUpdate extends LocaleEvent {
  LocaleUpdate(Locale locale) : super(locale);

  @override
  List<Object> get props => null;
}
