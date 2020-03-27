part of 'client.dart';

// ignore_for_file: non_constant_identifier_names
// ignore_for_file: must_be_immutable

@JsonSerializable()
class AppImage extends Equatable {
  String banner;
  String advertising;

  AppImage({this.banner, this.advertising});

  static AppImage fromJson(Map<String, dynamic> json) =>
      _$AppImageFromJson(json);
  Map<String, dynamic> toJson() => _$AppImageToJson(this);

  @override
  List<Object> get props => [banner, advertising];
}

@JsonSerializable()
class App extends Equatable {
  int id;
  AppImage image;
  int sorter;
  int tag;
  String app_size;
  String create_at;

  App({this.id, this.image, this.sorter, this.tag, this.create_at});

  static App fromJson(Map<String, dynamic> json) => _$AppFromJson(json);
  Map<String, dynamic> toJson() => _$AppToJson(this);

  @override
  List<Object> get props => [id];
}

class Result<T extends Object> {
  T result;

  Result({this.result});

  factory Result.fromJson(Map<String, dynamic> json, Function fromJson) {
    if (json['result'] is List) {
      return Result(
          result: json['result'].map<T>((f) => fromJson<App>(f)).toList());
    }
    return Result(result: fromJson(json));
  }
}
