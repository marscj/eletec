import 'package:dio/dio.dart';
import 'package:equatable/equatable.dart';
import 'package:rxdart/rxdart.dart';
import 'package:json_annotation/json_annotation.dart';
import 'package:retrofit/retrofit.dart';
import 'package:shared_preferences/shared_preferences.dart';

part 'app.dart';
part 'order.dart';
part 'client.g.dart';

class CacheService {
  static CacheService get instance => CacheService._();

  CacheService._();

  Future<String> getLanguage() async {
    return SharedPreferences.getInstance().then((sp) {
      return sp.getString('language') ?? 'en';
    });
  }

  Future<bool> setLanguage(language) async {
    return SharedPreferences.getInstance().then((sp) {
      return sp.setString('language', language);
    });
  }

  Future<String> getToken() async {
    return SharedPreferences.getInstance().then((sp) {
      return sp.getString('token') ?? 'unknow';
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

  Future<String> getAdvertising() {
    return SharedPreferences.getInstance().then((sp) {
      return sp.getString('ad');
    });
  }

  Future<bool> setAdvertising(ad) {
    return SharedPreferences.getInstance().then((sp) {
      return sp.setString('ad', ad);
    });
  }
}

//@RestApi(baseUrl: 'http://eletecapp.com/api')
@RestApi(baseUrl: 'http://127.0.0.1:8000/api')
abstract class RestService {
  static RestService get instance => _RestService(Dio(BaseOptions(
        connectTimeout: 5000,
        receiveTimeout: 3000,
      ))
        ..interceptors
            .add(new InterceptorsWrapper(onRequest: (Options options) async {
          var token = await CacheService.instance.getToken();
          options.headers['Authorization'] = token;
          return options;
        }, onResponse: (Response response) {
          response.data = response.data['result'];
          return response;
        }, onError: (DioError e) async {
          if (e?.response?.statusCode == 401) {
            CacheService.instance.clearToken();
          }
          return e;
        })));

  @GET("/apps/")
  Future<List<App>> getApps({@Queries() Map<String, dynamic> query});

  @GET("/orders/")
  Future<List<Order>> getOrders({@Queries() Map<String, dynamic> query});

  @GET("/orders/{id}/")
  Future<Order> getTask(@Path("id") String id);
}

class RestServiceExtra {
  static RestServiceExtra get instance => RestServiceExtra._();

  RestServiceExtra._();

  Stream<String> getAdvertising() {
    return Stream<String>.fromFutures([
      CacheService.instance.getAdvertising(),
      RestService.instance.getApps(query: {'tag': 0}).then((data) {
        var _data = data.isNotEmpty ? data?.last?.image?.advertising : null;
        CacheService.instance.setAdvertising(_data);
        return _data;
      })
    ]).delay(Duration(seconds: 10)).distinct();
  }
}
