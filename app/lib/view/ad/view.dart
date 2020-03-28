import 'package:eletec/rest/client.dart';
import 'package:eletec/view/ad/bloc/ad_bloc.dart';
import 'package:extended_image/extended_image.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

class AdPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Theme(
        data: ThemeData(
            brightness: Brightness.dark,
            backgroundColor: Colors.white,
            scaffoldBackgroundColor: Colors.white),
        child: Scaffold(
            body: Stack(children: <Widget>[
              Center(
                  child: StreamBuilder<String>(
                stream: RestServiceExtra.instance.getAdvertising(),
                builder:
                    (BuildContext context, AsyncSnapshot<String> snapshot) {
                  if (snapshot.hasData)
                    return ExtendedImage.network(snapshot.data,
                        fit: BoxFit.cover,
                        loadStateChanged: (ExtendedImageState state) {
                      switch (state.extendedImageLoadState) {
                        case LoadState.loading:
                          return Image.asset(
                            "assets/ad.jpg",
                            fit: BoxFit.cover,
                          );
                        case LoadState.completed:
                          return ExtendedRawImage(
                            image: state.extendedImageInfo?.image,
                            width: double.infinity,
                            height: double.infinity,
                            fit: BoxFit.cover,
                          );
                        default:
                          return null;
                          break;
                      }
                    });

                  return Image.asset('assets/ad.jpg', fit: BoxFit.cover);
                },
              )),
              SafeArea(
                  child: Container(
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
                          }, child: BlocBuilder<AdBloc, AdState>(
                                  builder: (context, state) {
                            return Text(
                              '${state.timer}',
                              style: TextStyle(color: Colors.white),
                            );
                          })))))
            ]),
            floatingActionButton: RaisedButton(
                onPressed: () {
                  RestServiceExtra.instance.getAdvertising();
                },
                child: Text('button'))));
  }
}
