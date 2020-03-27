import 'package:cached_network_image/cached_network_image.dart';
import 'package:eletec/model/model.dart';
import 'package:eletec/repository/app.dart';
import 'package:eletec/view/ad/bloc/ad_bloc.dart';
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

class AdPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) => Scaffold(
          body: SafeArea(
              child: Stack(children: <Widget>[
        Center(
            child: FutureBuilder<List<App>>(
          future: AppRepository().list({'tag': 0}),
          builder: (BuildContext context, AsyncSnapshot snapshot) {
            print(snapshot.data);
            return CachedNetworkImage(
                imageUrl: 'caonima',
                fadeOutDuration: Duration.zero,
                fadeInDuration: Duration.zero,
                imageBuilder: (context, imageProvider) => Container(
                    decoration: BoxDecoration(
                        image: DecorationImage(
                            image: imageProvider, fit: BoxFit.cover))),
                placeholder: (_, __) =>
                    Image.asset('assets/ad.jpg', fit: BoxFit.cover));
          },
        )),
        Container(
            alignment: Alignment.topRight,
            padding: const EdgeInsets.all(10),
            child: Container(
                alignment: Alignment.center,
                constraints: BoxConstraints.tight(Size(30, 30)),
                decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    color: Colors.grey.withOpacity(0.5)),
                child: BlocListener<AdBloc, AdState>(
                    listener: (context, state) {
                  if (state.timer == 0) {
                    // Router.instance.navigateTo(context, '/home', replace: true);
                  }
                }, child:
                        BlocBuilder<AdBloc, AdState>(builder: (context, state) {
                  return Text(
                    '${state.timer}',
                    style: TextStyle(color: Colors.white),
                  );
                })))),
        RaisedButton(
          onPressed: () {
            AppRepository().list({'tag': 0});
            BlocProvider.of<AdBloc>(context).add(AdEvent(5));
          },
          child: Text('button'),
        )
      ])));
}
