
import 'package:shared_preferences/shared_preferences.dart';

class Token {
  
  Token._();
  
  static Token instance = new Token._();

  Future<String> getToken() async {
    return SharedPreferences.getInstance().then((sp){
      return sp.getString('token');
    });
  }

  Future<bool> setToken(token) async {
    return SharedPreferences.getInstance().then((sp) {
      return sp.setString('token', token);
    });
  }
}