
import 'package:eletec/api/model.dart';
import 'package:eletec/api/request.dart';

final String GENERATE = "auth/phone/generate/";

class ApiService {

  // final String GENERATE = 'auth/phone/generate/';
  // final String Validate = 'auth/phone/validate/';
  // final String EmailValidate = 'auth/email/validate/';
  // final String Info = 'users/info/';
  // final String Logout = 'users/logout/';
  // final String Users = 'users/';
  // final String Contracts = 'contracts/';
  // final String Address = 'address/';
  // final String Skills = 'skills/';
  // final String WorkTimes = 'worktimes/';
  // final String Images = 'images/';
  // final String Orders = 'orders/';
  // final String Comments = 'comments/';
  // final String Faqs = 'faqs/';
  // final String Apps = 'apps/';
  // final String Applications = 'applications/';
  // final String Jobs = 'jobs/';

  Future<String> phoneGenerate(playload) {
    print('-----');
    return ApiRequest.instance.dio.get('auth/phone/generate/').then((res) {
      print(res);
      return null;
    });
  }

  Future<UserInfo> userInfo(playload) {
    return ApiRequest.instance.dio.get('/').then((res) {
      return new UserInfo();
    });
  }
}
