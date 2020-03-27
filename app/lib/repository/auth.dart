import 'package:eletec/repository/reponse.dart';
import 'package:eletec/repository/repository.dart';
import 'package:eletec/repository/request.dart';

class AuthRepository extends Repository {
  Future<Result> phoneGenerate(playload) {
    return ApiRequest.instance.dio.post('auth/phone/generate/',
        data: {'phone_number': '+9710557199186'}).then((res) {
      print(res);
      return null;
    });
  }

  Future<Result> phoneValidate(playload) {
    return ApiRequest.instance.dio.post('auth/phone/validate/').then((res) {
      print(res);
      return null;
    });
  }

  Future<Result> userInfo(playload) {
    return ApiRequest.instance.dio.get('users/info/').then((res) {
      return null;
    });
  }

  noSuchMethod(Invocation invocation) => super.noSuchMethod(invocation);
}
