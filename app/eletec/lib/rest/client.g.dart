// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'client.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

AppImage _$AppImageFromJson(Map<String, dynamic> json) {
  return AppImage(
    full: json['full'] as String,
    banner: json['banner'] as String,
    advertising: json['advertising'] as String,
  );
}

Map<String, dynamic> _$AppImageToJson(AppImage instance) => <String, dynamic>{
      'full': instance.full,
      'banner': instance.banner,
      'advertising': instance.advertising,
    };

App _$AppFromJson(Map<String, dynamic> json) {
  return App(
    id: json['id'] as int,
    image: json['image'] == null
        ? null
        : AppImage.fromJson(json['image'] as Map<String, dynamic>),
    sorter: json['sorter'] as int,
    tag: json['tag'] as int,
    create_at: json['create_at'] as String,
  )..app_size = json['app_size'] as String;
}

Map<String, dynamic> _$AppToJson(App instance) => <String, dynamic>{
      'id': instance.id,
      'image': instance.image,
      'sorter': instance.sorter,
      'tag': instance.tag,
      'app_size': instance.app_size,
      'create_at': instance.create_at,
    };

Otp _$OtpFromJson(Map<String, dynamic> json) {
  return Otp(
    json['phone_number'] as String,
  );
}

Map<String, dynamic> _$OtpToJson(Otp instance) => <String, dynamic>{
      'phone_number': instance.phone_number,
    };

Token _$TokenFromJson(Map<String, dynamic> json) {
  return Token(
    json['id'] as int,
    json['last_login'] as String,
    json['token'] as String,
  );
}

Map<String, dynamic> _$TokenToJson(Token instance) => <String, dynamic>{
      'id': instance.id,
      'last_login': instance.last_login,
      'token': instance.token,
    };

Order _$OrderFromJson(Map<String, dynamic> json) {
  return Order(
    id: json['id'] as int,
  );
}

Map<String, dynamic> _$OrderToJson(Order instance) => <String, dynamic>{
      'id': instance.id,
    };

// **************************************************************************
// RetrofitGenerator
// **************************************************************************

class _RestService implements RestService {
  _RestService(this._dio, {this.baseUrl}) {
    ArgumentError.checkNotNull(_dio, '_dio');
    this.baseUrl ??= 'http://127.0.0.1:8000/api/';
  }

  final Dio _dio;

  String baseUrl;

  @override
  getApps({query}) async {
    const _extra = <String, dynamic>{};
    final queryParameters = <String, dynamic>{};
    queryParameters.addAll(query ?? <String, dynamic>{});
    queryParameters.removeWhere((k, v) => v == null);
    final _data = <String, dynamic>{};
    final Response<List<dynamic>> _result = await _dio.request('/apps/',
        queryParameters: queryParameters,
        options: RequestOptions(
            method: 'GET',
            headers: <String, dynamic>{},
            extra: _extra,
            baseUrl: baseUrl),
        data: _data);
    var value = _result.data
        .map((dynamic i) => App.fromJson(i as Map<String, dynamic>))
        .toList();
    return Future.value(value);
  }

  @override
  getOrders({query}) async {
    const _extra = <String, dynamic>{};
    final queryParameters = <String, dynamic>{};
    queryParameters.addAll(query ?? <String, dynamic>{});
    queryParameters.removeWhere((k, v) => v == null);
    final _data = <String, dynamic>{};
    final Response<List<dynamic>> _result = await _dio.request('/orders/',
        queryParameters: queryParameters,
        options: RequestOptions(
            method: 'GET',
            headers: <String, dynamic>{},
            extra: _extra,
            baseUrl: baseUrl),
        data: _data);
    var value = _result.data
        .map((dynamic i) => Order.fromJson(i as Map<String, dynamic>))
        .toList();
    return Future.value(value);
  }

  @override
  getTask(id) async {
    ArgumentError.checkNotNull(id, 'id');
    const _extra = <String, dynamic>{};
    final queryParameters = <String, dynamic>{};
    final _data = <String, dynamic>{};
    final Response<Map<String, dynamic>> _result = await _dio.request(
        '/orders/$id/',
        queryParameters: queryParameters,
        options: RequestOptions(
            method: 'GET',
            headers: <String, dynamic>{},
            extra: _extra,
            baseUrl: baseUrl),
        data: _data);
    final value = Order.fromJson(_result.data);
    return Future.value(value);
  }

  @override
  phoneGenerate(playload) async {
    ArgumentError.checkNotNull(playload, 'playload');
    const _extra = <String, dynamic>{};
    final queryParameters = <String, dynamic>{};
    final _data = <String, dynamic>{};
    _data.addAll(playload ?? <String, dynamic>{});
    final Response<Map<String, dynamic>> _result = await _dio.request(
        '/auth/phone/generate/',
        queryParameters: queryParameters,
        options: RequestOptions(
            method: 'POST',
            headers: <String, dynamic>{},
            extra: _extra,
            baseUrl: baseUrl),
        data: _data);
    final value = Otp.fromJson(_result.data);
    return Future.value(value);
  }

  @override
  phoneValidate(playload) async {
    ArgumentError.checkNotNull(playload, 'playload');
    const _extra = <String, dynamic>{};
    final queryParameters = <String, dynamic>{};
    final _data = <String, dynamic>{};
    _data.addAll(playload ?? <String, dynamic>{});
    final Response<Map<String, dynamic>> _result = await _dio.request(
        '/auth/phone/validate/',
        queryParameters: queryParameters,
        options: RequestOptions(
            method: 'POST',
            headers: <String, dynamic>{},
            extra: _extra,
            baseUrl: baseUrl),
        data: _data);
    final value = Token.fromJson(_result.data);
    return Future.value(value);
  }
}
