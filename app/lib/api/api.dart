
import 'package:eletec/api/model.dart';
import 'package:eletec/api/reponse.dart';
import 'package:eletec/api/request.dart';
import 'package:eletec/cache/token.dart';

class ApiService {

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

  Future<Response> userInfo(playload) {
    return ApiRequest.instance.dio.get('/').then((res) {
      return null;
    });
  }
}
