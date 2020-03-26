part of 'locale.dart';

class LocaleBloc extends Bloc<LocaleEvent, LocaleState> {
  final String locale;

  LocaleBloc(this.locale);

  @override
  LocaleState get initialState => LocaleState(Locale(this.locale, ''));

  @override
  Stream<LocaleState> mapEventToState(LocaleEvent event) async* {
    if (event is LocaleInit) {
      var lan = await LanguageRepository().get();
      Locale locale = Locale(lan, '');
      yield LocaleState(locale);
    }

    if (event is LocaleUpdate) {
      Locale _locale = event.locale;

      await LanguageRepository().set(event.locale.languageCode);

      yield LocaleState(_locale);
    }
  }
}
