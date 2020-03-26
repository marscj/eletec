part of 'ad_bloc.dart';

abstract class AdEvent extends Equatable {
  AdEvent();

  @override
  List<Object> get props => [];
}

class AdStart extends AdEvent {
  final int timer;

  AdStart(this.timer);
}

class AdFinish extends AdEvent {}

class AdTimer extends AdEvent {
  final int timer;

  AdTimer(this.timer);
}
