import 'package:shared_preferences/shared_preferences.dart';

class LanguageRepository {
  Future<String> get() async {
    return SharedPreferences.getInstance().then((sp) {
      return sp.getString('language') ?? 'en';
    });
  }

  Future<bool> set(language) async {
    return SharedPreferences.getInstance().then((sp) {
      return sp.setString('language', language);
    });
  }
}
