class TenderBuilder:

    def __init__(self, app, data, file_path=None):
        self.app = app
        self.data = data
        self.file_path = file_path

    def create_tender_below_multi(self):
        app = self.app
        docs_of = ['tender', 'lot', 'item']
        app.home_page.select_create('tender')
        app.select_procedure_modal.select_procedure('belowThreshold')
        self.fill_tender()
        self.add_lot(0).add_lot(1)
        self.add_feature(0)
        app.tender_page.publish_tender(docs=True)
        for doc_of in docs_of:
            app.document_modal.attach_documents_tender(
                doc_of, 'biddingDocuments', self.data,
                self.file_path.format(file_name=doc_of + '.doc'))

    def fill_tender(self):
        app = self.app
        data = self.data
        app.tender_page.fill_tender_description(data)
        app.date_widget.fill_enquiry_period_end(data)
        app.date_widget.fill_tender_period_start(data)
        app.date_widget.fill_tender_period_end(data)

    def add_lot(self, index):
        app = self.app
        app.lot_modal.fill_lot(index, self.data)
        if index == 0:
            self.add_item(0).add_item(1)
        else:
            self.add_item(2).add_item(3)
        app.lot_modal.save_lot()
        return self

    def add_item(self, index):
        app = self.app
        data = self.data
        app.lot_modal.fill_item(index, data)
        app.lot_modal.select_cpv(index, data)
        app.lot_modal.fill_delivery_address(index, data)
        app.date_widget.fill_delivery_start(index, data)
        app.date_widget.fill_delivery_end(index, data)
        return self

    def add_feature(self, index):
        app = self.app
        data = self.data
        app.feature_modal.go_feature_modal()
        app.feature_modal.add_feature(index, data)


