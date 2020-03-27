abstract class Repository<T> {
  Future<T> list(Map<String, dynamic> params);

  Future<T> get(int pk);

  Future<T> post(Map<String, dynamic> playload);

  Future<T> put(int pk, Map<String, dynamic> playload);

  Future<T> del(int pk);

  // Future<T> list({Map<String, dynamic> params}) {
  //   return ApiRequest.instance.dio.get(path, queryParameters: params);
  // }

  // Future<Response> get(int pk) {
  //   return ApiRequest.instance.dio.get(path + '/$pk/');
  // }

  // Future<Response> post(Map<String, dynamic> playload) {
  //   return ApiRequest.instance.dio.post(path, data: playload);
  // }

  // Future<Response> put(int pk, Map<String, dynamic> playload) {
  //   return ApiRequest.instance.dio.put(path + '/$pk/', data: playload);
  // }

  // Future<Response> del(int pk) {
  //   return ApiRequest.instance.dio.delete(path + '/$pk/');
  // }
}
