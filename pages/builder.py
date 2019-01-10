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
        self.add_lot(0).fill_item(0).add_item(1)
        app.lot_form.save_lot()
        self.add_lot(1).fill_item(2)
        app.lot_form.save_lot()
        self.add_feature(0)
        app.tender_page.publish_tender(docs=True)
        for doc_of in docs_of:
            app.document_form.attach_documents_tender(
                doc_of, 'biddingDocuments', self.data,
                self.file_path.format(file_name=doc_of + '.doc'))

    def fill_tender(self):
        app = self.app
        data = self.data
        app.tender_page.fill_tender_description(data)
        app.date_widget.fill_tender_periods(data)

    def add_lot(self, index):
        app = self.app
        app.tender_page.go_lot_form()
        app.lot_form.fill_lot(index, self.data)
        return self

    def fill_item(self, index):
        app = self.app
        data = self.data
        app.item_form.fill_item(index, data)
        app.item_form.select_cpv(index, data)
        app.item_form.fill_delivery_address(index, data)
        app.date_widget.fill_delivery_periods(index, data)
        return self

    def add_item(self, index):
        app = self.app
        app.item_form.go_item_form()
        self.fill_item(index)
        return self

    def add_feature(self, index):
        app = self.app
        data = self.data
        app.feature_form.go_feature_form()
        app.feature_form.add_feature(index, data)


