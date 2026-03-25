package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Describes an individual finding.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Finding  {

  private String uuid;
  private String title;
  private String description;
  private FindingTarget target;
  private String implementation-statement-uuid;
  private List<Origin> origins;
  private List<RelatedObservation> related-observations;
  private List<AssociatedRisk> related-risks;
  private String remarks;
  private List<Property> props;
  private List<Link> links;

}