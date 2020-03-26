import 'package:eletec/config/router.dart';
import 'package:eletec/view/ad/bloc/ad_bloc.dart';
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

class AdPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) =>
      BlocListener<AdBloc, AdState>(listener: (context, state) {
        if (state is AdEnd) {
          Router.instance.router.navigateTo(context, '/home', replace: true);
        }
      }, child: BlocBuilder<AdBloc, AdState>(builder: (context, state) {
        return Container();
      }));
}
