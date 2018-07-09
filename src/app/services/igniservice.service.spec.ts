import { TestBed, inject } from '@angular/core/testing';

import { IgniserviceService } from './igniservice.service';

describe('IgniserviceService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [IgniserviceService]
    });
  });

  it('should be created', inject([IgniserviceService], (service: IgniserviceService) => {
    expect(service).toBeTruthy();
  }));
});
