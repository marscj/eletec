// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'model.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

AppImage _$AppImageFromJson(Map<String, dynamic> json) {
  return AppImage(
    json['banner'] as String,
    json['advertising'] as String,
  );
}

Map<String, dynamic> _$AppImageToJson(AppImage instance) => <String, dynamic>{
      'banner': instance.banner,
      'advertising': instance.advertising,
    };

App _$AppFromJson(Map<String, dynamic> json) {
  return App(
    json['id'] as int,
    json['image'] == null
        ? null
        : AppImage.fromJson(json['image'] as Map<String, dynamic>),
    json['sorter'] as int,
    json['tag'] as int,
    json['create_at'] as String,
  );
}

Map<String, dynamic> _$AppToJson(App instance) => <String, dynamic>{
      'id': instance.id,
      'image': instance.image,
      'sorter': instance.sorter,
      'tag': instance.tag,
      'create_at': instance.create_at,
    };
