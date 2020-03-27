import 'package:eletec/repository/repository.dart';
import 'package:eletec/repository/request.dart';

class AuthRepository extends Repository {
  Future<String> phoneGenerate(playload) {
    return ApiRequest.instance.dio.post('auth/phone/generate/',
        data: {'phone_number': '+9710557199186'}).then((res) {
      print(res);
      return null;
    });
  }

  Future<String> phoneValidate(playload) {
    return ApiRequest.instance.dio.post('auth/phone/validate/').then((res) {
      print(res);
      return null;
    });
  }

  Future<String> userInfo(playload) {
    return ApiRequest.instance.dio.get('users/info/').then((res) {
      return null;
    });
  }

  noSuchMethod(Invocation invocation) => super.noSuchMethod(invocation);
}
