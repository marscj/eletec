import 'package:dio/dio.dart';
import 'package:rxdart/rxdart.dart';
import 'package:json_annotation/json_annotation.dart';
import 'package:retrofit/retrofit.dart';
import 'package:shared_preferences/shared_preferences.dart';

part 'app.dart';
part 'order.dart';
part 'client.g.dart';

class DioService {
  Dio dio;

  DioService._() {
    BaseOptions options = new BaseOptions(
      // baseUrl: 'http://eletecapp.com/api/',
      baseUrl: 'http://127.0.0.1:8000/api/',
      connectTimeout: 5000,
      receiveTimeout: 3000,
    );

    dio = new Dio(options)
      ..interceptors
          .add(new InterceptorsWrapper(onRequest: (Options options) async {
        var token = await CacheService.instance.getToken();
        options.headers['Authorization'] = token;
        return options;
      }, onError: (DioError e) async {
        if (e?.response?.statusCode == 401) {
          CacheService.instance.clearToken();
        }
        return e;
      }));
  }

  static DioService instance = new DioService._();
}

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

@RestApi()
abstract class RestService {
  // factory RestClient(Dio dio, {String baseUrl}) = _RestClient;

  static RestService get instance => _RestService(DioService.instance.dio);

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
    return Stream.fromFutures([
      CacheService.instance.getAdvertising(),
      RestService.instance.getApps(query: {'tag': 0}).then((data) {
        var _data = data.isNotEmpty ? data?.last?.image?.advertising : null;
        CacheService.instance.setAdvertising(_data);
        return _data;
      })
    ]);
  }
}
