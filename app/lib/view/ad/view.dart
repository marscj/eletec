import 'package:eletec/view/ad/bloc/ad_bloc.dart';
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

class AdPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return BlocProvider<AdBloc>(
        create: (_) => AdBloc(),
        child: BlocBuilder<AdBloc, AdState>(builder: (context, state) {
          return Material(
            child: Center(child: Text('${state.timer}')),
          );
        }));
  }
}
