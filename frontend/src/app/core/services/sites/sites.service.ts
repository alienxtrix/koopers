import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import {Site} from '../../models/sites'
import { environment } from '../../../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class SitesService {
  constructor(private http: HttpClient) {}

  getSites(): Observable<Site[]> {
    return of(
      [
        {
            "id": 1,
            "title": "El universal",
            "url": "https://www.eluniversal.com.co/",
            "available": true,
            "created": "2020-09-21T12:54:09.759990-05:00",
            "updated": "2020-09-21T12:54:09.759990-05:00"
        },
        {
            "id": 2,
            "title": "New York Times",
            "url": "https://www.nytimes.com/es/",
            "available": true,
            "created": "2020-09-21T12:55:01.239635-05:00",
            "updated": "2020-09-21T12:55:01.239635-05:00"
        },
        {
            "id": 3,
            "title": "Washington Post",
            "url": "https://www.washingtonpost.com/",
            "available": false,
            "created": "2020-09-21T12:55:51.647464-05:00",
            "updated": "2020-09-21T12:55:51.647464-05:00"
        },
    ]
    )
    // return this.http.get(`${environment.url_api}/api/sites`);
  }
}
