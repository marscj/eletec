import 'package:shared_preferences/shared_preferences.dart';

class TokenRepository {
  Future<String> get() async {
    return SharedPreferences.getInstance().then((sp) {
      return sp.getString('token') ?? 'unknow';
    });
  }

  Future<bool> set(token) async {
    return SharedPreferences.getInstance().then((sp) {
      return sp.setString('token', 'token ' + token);
    });
  }

  Future<bool> clear() async {
    return SharedPreferences.getInstance().then((sp) {
      return sp.remove('token');
    });
  }
}
