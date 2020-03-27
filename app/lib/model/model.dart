import 'package:json_annotation/json_annotation.dart';
part 'model.g.dart';

// ignore_for_file: non_constant_identifier_names

@JsonSerializable()
class AppImage {
  String banner;
  String advertising;

  AppImage({this.banner, this.advertising});

  factory AppImage.fromJson(Map<String, dynamic> json) =>
      _$AppImageFromJson(json);
  Map<String, dynamic> toJson() => _$AppImageToJson(this);
}

@JsonSerializable()
class App {
  int id;
  AppImage image;
  int sorter;
  int tag;
  String app_size;
  String create_at;

  App({this.id, this.image, this.sorter, this.tag, this.create_at});

  factory App.fromJson(Map<String, dynamic> json) => _$AppFromJson(json);
  Map<String, dynamic> toJson() => _$AppToJson(this);
}
