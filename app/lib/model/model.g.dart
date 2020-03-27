// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'model.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

AppImage _$AppImageFromJson(Map<String, dynamic> json) {
  return AppImage(
    banner: json['banner'] as String,
    advertising: json['advertising'] as String,
  );
}

Map<String, dynamic> _$AppImageToJson(AppImage instance) => <String, dynamic>{
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
