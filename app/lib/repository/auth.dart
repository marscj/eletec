import 'package:eletec/repository/reponse.dart';
import 'package:eletec/repository/request.dart';
import 'package:shared_preferences/shared_preferences.dart';

class AuthRepository {
  Future<Response> phoneGenerate(playload) {
    return ApiRequest.instance.dio.post('auth/phone/generate/', data: {'phone_number': '+9710557199186'}).then((res) {
      print(res);
      return null;
    });
  }

  Future<Response> phoneValidate(playload) {
    return ApiRequest.instance.dio.post('auth/phone/validate/').then((res) {
      print(res);
      return null;
    });
  }

  Future<String> getToken() async {
    return SharedPreferences.getInstance().then((sp){
      return sp.getString('token');
    });
  }

  Future<bool> setToken(token) async {
    return SharedPreferences.getInstance().then((sp) {
      return sp.setString('token', 'token ' + token);
    });
  }

  Future<bool> clearToken() async {
    return SharedPreferences.getInstance().then((sp) {
      return sp.remove('token');
    });
  }

  Future<Response> userInfo(playload) {
    return ApiRequest.instance.dio.get('users/info/').then((res) {
      return null;
    });
  }
}

class UserRepository {

}