part of 'locale_bloc.dart';

abstract class LocaleEvent extends Equatable {
  @override
  List<Object> get props => [];
}

class LocaleInit extends LocaleEvent {}

class LocaleUpdate extends LocaleEvent {
  final Locale locale;

  LocaleUpdate(this.locale);
}
