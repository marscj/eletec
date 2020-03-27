part of 'client.dart';

// ignore_for_file: non_constant_identifier_names
// ignore_for_file: must_be_immutable
// ignore_for_file: undefined_method

@JsonSerializable()
class AppImage extends Equatable {
  String banner;
  String advertising;

  AppImage({this.banner, this.advertising});

  factory AppImage.fromJson(Map<String, dynamic> json) =>
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

  factory App.fromJson(Map<String, dynamic> json) => _$AppFromJson(json);
  Map<String, dynamic> toJson() => _$AppToJson(this);

  @override
  List<Object> get props => [id];
}

class Result<T> {
  T result;

  Result(this.result);

  factory Result.fromJson(Map<String, dynamic> json) {
    if (T is List) {
      return T.map((f) => f.fromJson(json)).toList();
    }

    return T.fromJson(json);
  }
}
