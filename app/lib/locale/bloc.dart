part of 'locale.dart';

class LocaleBloc extends Bloc<LocaleEvent, LocaleState> {
  @override
  LocaleState get initialState => LocaleState(Locale('en', ''));

  @override
  Stream<LocaleState> mapEventToState(LocaleEvent event) async* {
    if (event is LocaleInit) {
      Locale locale = Locale(await LanguageRepository().getLanguage(), '');
      yield LocaleState(locale);
    }
  }
}
